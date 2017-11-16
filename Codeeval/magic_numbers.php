//55
<?php

	function isMagic($s)
	{		
		$l = strlen($s);

		if (strlen(count_chars( $s, 3)) != $l)
		{
			return false;
		}

		$visited = array();		
		$a = $b = intval($s[0]);
		$j = 0;
		while( ! in_array($b,$visited))
		{
			
			$visited[] = $b;
			
			$j = ($b + $j)%$l;
			$b = intval($s[$j]);
			
		}



		if (($a == $b) & (count($visited)==$l))
		{
			return true;
		}
		else
		{
			return false;
		}	

	}

	

	

	

	$allMagics = array();
	for ($x=1;$x<10001;$x++)
	{
		$allMagics[$x] = isMagic(strval($x));
	}
	
	

	

	$fh = fopen($argv[1], "r");	
	while (!feof($fh))
	{
		$ins = array_map("intval",explode(" ",fgets($fh)));
		$a = $ins[0];
		$b = $ins[1];
		$mset = array();
		
		for ($i=$a;$i<=$b;$i++)
		{
			if($allMagics[$i])
			{
				$mset[]= $i;
			}
		}
		if (count($mset)>0)
		{
			echo implode(" ",$mset);
			
		}
		else
		{
			echo "-1";
		}
		echo PHP_EOL;
		
	}
	
