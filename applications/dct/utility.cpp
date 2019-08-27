#include "echoserver.h"
#include <Properties/propertiesfile.h>
#include <circle/alloc.h>
#include <circle/util.h>
#include <benchmark.h>
#include <circle/logger.h>
#include <circle/net/in.h>
#include <circle/cputhrottle.h>
#include <circle/sched/scheduler.h>


#define CHAR_T 0
#define INT_T 1
#define FLOAT_T 2
#define UCHAR_T 3


unsigned totalCycles[4*7];
unsigned currentFreq;
static const char FromEcho[] = "echo";

double COS[] = { 1.0,0.98078528040323043,0.92387953251128674,0.83146961230254524,0.70710678118654757,0.55557023301960229,0.38268343236508984,0.19509032201612833,1.0,0.83146961230254524,0.38268343236508984,-0.19509032201612819,-0.70710678118654746,-0.98078528040323043,-0.92387953251128685,-0.55557023301960218,1.0,0.55557023301960229,-0.38268343236508973,-0.98078528040323043,-0.70710678118654768,0.1950903220161283,0.92387953251128652,0.83146961230254546,1.0,0.19509032201612833,-0.92387953251128674,-0.55557023301960218,0.70710678118654735,0.83146961230254546,-0.38268343236508989,-0.98078528040323065,1.0,-0.19509032201612819,-0.92387953251128685,0.55557023301960184,0.70710678118654768,-0.83146961230254512,-0.38268343236509056,0.98078528040323043,1.0,-0.55557023301960196,-0.38268343236509034,0.98078528040323043,-0.70710678118654668,-0.19509032201612803,0.92387953251128674,-0.83146961230254501,1.0,-0.83146961230254535,0.38268343236509,0.19509032201612878,-0.70710678118654713,0.98078528040323065,-0.92387953251128641,0.55557023301960151,1.0,-0.98078528040323043,0.92387953251128652,-0.83146961230254512,0.70710678118654657,-0.55557023301960151,0.38268343236508956,-0.19509032201612858 };

double C[] = { 0.70710678118654746,1,1,1,1,1,1,1 };



void CEchoServer::sendResults(){
    float temp =CCPUThrottle::Get ()->GetTemperature () ;
    unsigned int freq = currentFreq;
    int type = FLOAT_T;
    int elements=OUTPUT_SIZE;
    int remaining_bytes = elements;
    int bytes=0;
    int pos = 0;

    CLogger::Get ()->Write (FromEcho, LogNotice, "Elements %d",elements);

    if (m_pSocket->Send (&temp, sizeof(float) , MSG_DONTWAIT) != sizeof(float))
    {
        CLogger::Get ()->Write (FromEcho, LogPanic, "Cannot send temperature");
    }
    if (m_pSocket->Send (&freq, sizeof(int) , MSG_DONTWAIT) != sizeof(float))
    {
        CLogger::Get ()->Write (FromEcho, LogPanic, "Cannot send frequency");
    }
    if (m_pSocket->Send (&type,sizeof(int) , MSG_DONTWAIT) != sizeof(int))
    {
        CLogger::Get ()->Write (FromEcho, LogPanic, "Cannot send result type");
    }
    if (m_pSocket->Send (&elements,sizeof(int) , MSG_DONTWAIT) != sizeof(int))
    {
        CLogger::Get ()->Write (FromEcho, LogPanic, "Cannot send number of elements");
    }

    if (m_pSocket->Send (totalCycles,4*7*sizeof(int) , MSG_DONTWAIT) != 4*7*sizeof(int))
    {
        CLogger::Get ()->Write (FromEcho, LogPanic, "Cannot send number of Cycles");
    }

    //This is where i send the real results to the coordinator
    while ( pos < elements ){
        bytes = FRAME_BUFFER_SIZE/sizeof(OUTPUT_TYPE);
        if ( (remaining_bytes - pos ) < (FRAME_BUFFER_SIZE)/sizeof(OUTPUT_TYPE) )
            bytes = remaining_bytes - pos;
        if (m_pSocket->Send (&output[pos] ,sizeof(OUTPUT_TYPE)*bytes , MSG_DONTWAIT) != bytes * sizeof(OUTPUT_TYPE))
        {
            CLogger::Get ()->Write (FromEcho, LogPanic, "Cannot send number results");
        }
        pos = pos + bytes ;

    }
    return;
}


void CEchoServer::ReadInput (void){

    unsigned fd;
    unsigned int i,j;
    unsigned nResult;
    const unsigned smallSize = 512;
    unsigned char *buffer = (unsigned char *) malloc ( smallSize*smallSize) ;

    CLogger::Get ()->Write (FromEcho, LogNotice, "Malloced");
    if ( input == 0 )
        return;
    fd = m_FileSystem->FileOpen("input.grey");

    if ( fd == 0 ){
        CLogger::Get ()->Write (FromEcho, LogPanic, "Cannot open file: input.grey");
    }

    nResult = m_FileSystem->FileRead(fd,buffer,smallSize*smallSize);
    if ( nResult == FS_ERROR ){
        CLogger::Get ()->Write (FromEcho, LogPanic, "Cannot read file: input.grey");
    }

    CLogger::Get ()->Write (FromEcho, LogNotice, "Read Input");
    if (!m_FileSystem->FileClose (fd))
    {
        CLogger::Get ()->Write (FromEcho, LogPanic, "Cannot close file");
    }

    for ( i = 0 ; i < SIZE ; i++ ){
        for ( j = 0; j < SIZE/smallSize ; j++){
          memcpy( &input [ i * SIZE + j *smallSize ], &buffer [ (i % smallSize) *smallSize ], sizeof(char) * smallSize);
        }
      }

    return;
}



