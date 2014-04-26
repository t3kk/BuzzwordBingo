/*Functions for the bingo game*/

function bingoCellClicked(clickedId)
{
	toggleColor(clickedId);
	checkForWin(clickedId);
}

function toggleColor(clickedId)
{
	if (document.getElementById(clickedId).style.backgroundColor!="red")
	{
		document.getElementById(clickedId).style.backgroundColor="red";
	}
	else
	{
		document.getElementById(clickedId).style.backgroundColor="white";
	}
}

function checkForWin(clickedId)
{
	var coords = extractCoordinates(clickedId);
	alert(coords.x+" "+coords.y);
}

function extractCoordinates(clickedId)
{
	//Used txt2re.com to make this function cause its soo redicilously easy.  Please suggest improvements if you notice them.
	var re1='.*?';	// Non-greedy match on filler
    var re2='(\\d+)';	// Integer Number 1
    var re3='.*?';	// Non-greedy match on filler
    var re4='(\\d+)';	// Integer Number 2
    var p = new RegExp(re1+re2+re3+re4,["i"]);
    var m = p.exec(clickedId);
    return {x:m[1], y:m[2]}
}