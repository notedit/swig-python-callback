/* File : example.i */
%module(directors="1") example
%{
#include "example.h"
%}

/* turn on director wrapping Callback */
%feature("director") Callback;
%feature("director") CallbackBase;

%include "example.h"

