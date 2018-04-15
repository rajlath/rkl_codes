def get_sum (psum, ss, k, N):

      # bit devide by value
    l = psum [0]
    r = psum [-1 ]
    while l + 1 < r:
        mid = (l + r) / 2
        count = 0
        lp = 0
        rp = 1
        for lp in xrange (N):
            while rp <= N and psum [rp] - psum [lp] <= mid:
                rp + = 1
                count + = rp - lp -1
                if count < k:
                    l = mid
                elif count> k:
                    r = mid
                else :
                    break
     if l + 1 < r:
          l = mid # use l as the finally calculate element
     else :
          lp = 0
          rp = 1
          count = 0
          for lp in xrange (N):
              while rp <= N and psum [rp] - psum [lp] <= l:
                  rp + = 1
              count + = rp - lp -1
         if count <k: # make sure that l is the first value that make the count larger or equal to k, l is not qualified, count r's number
             l = r
              lp = 0
              rp = 1
              count = 0
              for lp in xrange (N):
                  while rp <= N and psum [rp] - psum [lp] <= l:
                      rp + = 1
                  count + = rp - lp -1
 # how to calculate the last output
     lp = 0
      rp = 1
      ans = 0
      for lp in xrange (N):
          while rp <= N and psum [rp] - psum [lp] <= l:
              rp + = 1
          ans + = ss [rp-1] - ss [lp] - (rp-lp-1) * psum [lp]
      ans - = (count - k) * l

      return ans

  input  = open ('D-large-practice.in ' , ' r ' )
  output = open ('D-large-practice.out ' , ' w ' )
  T = int (input.readline (). Strip ())
  for n in xrange (T):
      output.writelines ( ' Case #% s: \ n ' % (n + 1 ))
      N, Q = map (int, input.readline (). Strip (). Split ())
      array = map (int, input.readline (). strip (). split ())
      psum = [0]
      ss = [0]
      for i in array:
          psum.append (psum [ -1] + i)
      for i in psum [1 :]: # remove the dummy
          ss.append (ss [ -1] + i)
      for j in xrange (Q):
          l, r = map (int, input.readline (). strip (). split ())
          output.writelines ( ' % s \ n ' % (get_sum (psum, ss, r, N) -get_sum (psum, ss, 1-1, N)))