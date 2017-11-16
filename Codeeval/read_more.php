<?php

	$fh = fopen($argv[1],'r');
	

	while(! feof($fh) )
	{
		$testcase = trim(fgets($fh));
		if($testcase == "") continue;
		

		if(strlen($testcase) <= 55)
		{
			echo $testcase;
			echo PHP_EOL;
		}
		else
		{
			$out = substr($testcase,0,40);	
			
			if(strrpos($out,' ') != False)
			{
				$lastspc = strrpos($out,' ');
				$out = substr($out, 0,$lastspc);

			}

			echo $out."... <Read More>";
			echo PHP_EOL;
			
		}
		
	}


	function count_array_size($lines)
	{
		$cnt = 0;
		foreach($lines as $line)
		{
			$cnt += strlen($line);
		}
		return $cnt;
	}
