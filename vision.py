import motor
import color detector
import qr_scanner
import ir
import us

ideal_qr_us_dist=19.5


def check_for_block():
    if color detector.color()!=white :
        return True

#this is so wrong rajat
def scan_qr():
    time=0.1
    Thread( target=qr_scanner.scan)
    time.sleep(0.5)
    while True:
        error=ideal_qr_us_dist-us.dist(qr_trig,qr_echo)
        diff_error=(error-last_error)/feedback_loop.delay
        last_error=error
         
        Kp=0.5
        Kd=0.25
        P=Kp*error
        D=Kd*diff_error
        pid_value=P+D
         
        if us.dist(qr_trig,qr_echo)<ideal_qr_us_dist:
            motor.set_speed('b',-40-pid_value)
            time.sleep(0.25)
            motor.set_speed('b',0)             
        qr_read=open('qr_result.txt','r')
        s=qr_read.read()

        time+=0.02
        else:
            motor.set_speed('r',-60)
            time.sleep(time)
            motor.sleep('b',0)
            time.sleep(0.5)
            motor.set_speed('r',60)
            time.sleep(time)
            motor.sleep('b',0)
            time.sleep(0.5)
            motor.set_speed('l',-60)
            time.sleep(time)
            motor.sleep('b',0)
            time.sleep(0.5)
            motor.sleep('l',60)
            time.sleep(time)
            motor.sleep('b',0)
            time.sleep(0.5)
            motor.set_speed('b',0)
        
        if not s='':

            break

            
    return True

def ground_is_white():
    if ir.loop()=="black":
        return False
    else:
        return True

    