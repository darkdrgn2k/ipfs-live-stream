<?php
$r=$_REQUEST["gw"];

if ($r=="") $r="https://ipfs.io";

?>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="video-js.min.css" rel="stylesheet">
<script src="video.min.js"></script>
<script src="videojs-contrib-hls.min.js"></script>
<style>
html, body, #live { width:100%; height:100%;  margin:0; padding:0;}
</style>
</head>
<body>
<script>window.HELP_IMPROVE_VIDEOJS = false;</script>
<video id="live" width="100%" height="100%" class="video-js vjs-default-skin" controls>
	<source src="playlist.php?gw=<?=$r?>" type="application/x-mpegURL">
</video>
<script>
  var player = videojs('#live');
</script>
</body>
</html>
