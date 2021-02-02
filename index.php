
<html>
<style>
body {
    font-family: Consolas, Menlo, Monaco, Lucida Console, Liberation Mono, DejaVu Sans Mono, Bitstream Vera Sans Mono, Courier New, monospace, serif;
}
</style>
<body>
<?php

$dir_title = basename(__DIR__);

echo '<h1>./'.$dir_title.'</h1>';

$files = glob('*', GLOB_BRACE);
foreach($files as $file) {
	if($file != "download-doujins.py")
	    if($file != "index.php")
		    echo '<br>* <a href="'.$file.'">'.$file.'</a>';
}
?>
</body>
</html>