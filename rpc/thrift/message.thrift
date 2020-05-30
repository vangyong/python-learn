namespace java cn.segema.learn.message
namespace py message

service MessageService {
    void ping();
    string sayHello();
    bool sendMobileMessage(1:string mobile,2:string message);
    bool sendEmailMessage(1:string email, 2:string message);
}