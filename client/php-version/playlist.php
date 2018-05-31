<?php

header("Cache-Control: no-store, no-cache, must-revalidate, max-age=0");
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache");

header('Access-Control-Allow-Origin: *');
//include ("test.m3u8");



$s=file_get_contents("playlist.m3u8");
if (isset($_REQUEST["gw"])) {
$s=str_replace("https://ipfs.io",$_REQUEST["gw"],$s);

}

echo $s;

