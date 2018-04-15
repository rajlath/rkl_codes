f=pryr::f(+`if`(x<5,x!=1,f(x-2)+f(x-3)+f(x-5)))
cat(f{as.integer(readline())})