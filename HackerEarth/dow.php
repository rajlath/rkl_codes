<?php
   $input = unixtojd(mktime(0, 0, 0, 8, 16, 1519));
   print_r(cal_from_jd($input, CAL_GREGORIAN));
?>