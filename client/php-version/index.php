<html>
<head>
<script>
var l=Array();
var s=Array();
i=0;
l[i++]="http://rx14.co.uk";
l[i++]="https://ipfs.io";
l[i++]="https://gateway.ipfs.io";
l[i++]="https://ipfs.infura.io";
l[i++]="https://xmine128.tk";
l[i++]="https://ipfs.jes.xxx";
l[i++]="https://siderus.io";
l[i++]="https://www.eternum.io";
l[i++]="https://hardbin.com";
l[i++]="https://ipfs.macholibre.org";
l[i++]="https://ipfs.works";
l[i++]="https://ipfs.work";
l[i++]="https://ipfs.wa.hle.rs";
l[i++]="https://upload.global";
l[i++]="https://api.wisdom.sh";
l[i++]="https://h.ipfs.io";
l[i++]="http://h.groundupworks.com";

l[i++]="http://127.0.0.1:8080";

function Test(url,index) {
	s[index]=performance.now();
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     TestComplete(url,index,this.responseText);
    }
  };

  xhttp.open("GET", url + "/ipfs/Qmaisz6NMhDB51cCvNWa1GMS7LU1pAxdF4Ld6Ft9kZEP2a", true);
  xhttp.send();
}
function TestComplete(url,index,what) {

	var isvalid=0;
	if ( what == "Hello from IPFS Gateway Checker\n" ) { 
		var speed= performance.now() - s[index];
		tmp.innerHTML=tmp.innerHTML + ("<a href='/tv/watch.php?gw=" + url + "'>" + url + "</a> ( " + speed  + " ms)<br>");
	}
}



</script>

</head>
<body>

<div id="gateway">
<h1>Select a hw</h1>
</div>

<script>

var tmp=document.getElementById("gateway");
for (var a=0; a < i; a++) {
Test(l[a],a);
}

</script>
</body>
</html>
