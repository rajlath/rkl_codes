<?php
header('Content-Type: text/plain; charset=utf-8');
if( isset($_GET['f_i_l_e']) && $_GET['f_i_l_e'] ) $argv[1] = $_GET['f_i_l_e'];
if( isset($argv[1]) && $argv[1] ){
    $filename = $argv[1];
    $fp = fopen($filename, 'r');
    $max_distance = 10000 * 10000 + 1;
    $points = array();
    
    function point_cmp($a,$b){  return $a[0] - $b[0]; }
    
    while ( $fp && !feof( $fp ) ) {
		 $line = trim(fgets($fp));
		 if( $points ){
			 $distance = $max_distance;
             $cnt = count($points);
             usort($points, 'point_cmp');
             for($i=0, $max=$cnt-1 ; $i < $max ; $i++){
				 for($j = $i+1; $j < $cnt ; $j++){					 
                     $x0 = $points[$i][0];                     
                     $x1 = $points[$j][0];
                     $xd = $x1 - $x0; 
                     if( $xd * $xd > $max_distance ){
						 break;
					 } //distance greater than max
                     $y0 = $p0[1];
                     $y1 = $p1[1];
                     $yd = $y1 - $y0; 
                     $ds = $xd * $xd + $yd * $yd;
                     if( $ds < $distance ){
							$max_distance = $ds;
                         }//update max distance
					 
				 
				}// for end j
				echo ( ( $distance >= $max_distance ) ? 'INFINITY' : sprintf('%.04f', round(sqrt($distance),4) ) ) . "\n";				
			 }// for end i
			 $points = array();
		 } else{
			 $points[] = explode(' ',$line);
		 	
	}//end opening file
	fclose( $fp );
	}
}	
