def hex_to_binary():
    with open("data054.bin") as f:
        for i in range(1,2041):
            with open("binary" + str(i) + ".txt", "w") as file:
                counter = 0
                while counter < 16384:
                    c = f.read(1)
                    hex_version = "0x" + c

                    if not c:
                        break
                    file.write(bin(int(hex_version, 16))[2:])
                    
                    counter += 4

def prepare_faults():
    totalErrors = 0
    for i in range(1,2041):
        with open("binary" + str(i) + ".txt") as file:
            counter = 0
            numErrors=0
            while True:
                c = file.read(1)
                if c == "0":
                    numErrors+=1
                    totalErrors+=1
                    cache_line = int(counter / 512)
                    bit_offset_from_cache_line = counter % 512
                    byte_offset = int(bit_offset_from_cache_line / 8)
                    bit_offset_from_byte = bit_offset_from_cache_line % 8
                    with open("bram" + str(i) + ".txt", "a") as output:
                        output.write('%s %s %s l1d\n' % (str(cache_line), str(byte_offset), str(bit_offset_from_byte)))

                if not c:
                    break
                counter += 1
            if numErrors !=0:
                print (numErrors)
    print ("Total Errors are ", totalErrors)
                
            
if __name__ == "__main__":
    hex_to_binary()

    prepare_faults()
