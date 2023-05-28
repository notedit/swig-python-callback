/* File : example.h */

#include <iostream>




class CallbackBase {
public:
	virtual void run() = 0;
};


class Callback : public CallbackBase {
public:
	virtual ~Callback() { std::cout << "Callback::~Callback()" << std:: endl; }
	virtual void run() { std::cout << "Callback::run()" << std::endl; }
};


class Caller {
private:
	CallbackBase *_callback;
public:
	Caller(): _callback(0) {}
	~Caller() { delCallback(); }
	void delCallback() { delete _callback; _callback = 0; }
	void setCallback(Callback *cb) { 
		delCallback(); 
		_callback = cb;

		_callback->run();	
	}
	void call() { if (_callback) _callback->run(); }
};

