#ifndef STATUS_H
#define STATUS_H

#include <string>

namespace templat {

class Status {
protected:
    /* data */
    enum Code {
        InternalError = -1,
        Ok = 0,
    };

public:
    Status() : _code(Ok), _msg(""){}

    Status(const Code& code, const std::string& msg) : _code(code), _msg(msg) {}

    ~Status() {}

    static Status OK() {
        Status ok = Status();
        return ok;
    }
    static Status Error(const std::string& msg) {
        Status internal_error = Status(InternalError, msg);
        return internal_error;
    }

    std::string msg() const {
        return _msg;
    }

    bool ok() const {
        return Ok == _code;
    }

protected:
    Code _code;
    std::string _msg;
};

} // namespace templat


#endif