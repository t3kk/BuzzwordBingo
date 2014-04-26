/*Functions for the bingo game*/

var CHECKED_COLOR = "#6495ED";  /* Can we get the icon in cornflower blue https://www.youtube.com/watch?v=746j4dN1sQg */
var UNCHECKED_COLOR = "white";

function bingoCellClicked(clickedId)
{
	toggleColor(clickedId);
	checkForWin(clickedId);
}

function toggleColor(clickedId)
{
	if (document.getElementById(clickedId).style.backgroundColor!=CHECKED_COLOR)
	{
		document.getElementById(clickedId).style.backgroundColor=CHECKED_COLOR;
	}
	else
	{
		document.getElementById(clickedId).style.backgroundColor=UNCHECKED_COLOR;
	}
}

function checkForWin(clickedId)
{
	var coords = extractCoordinates(clickedId);
	//check the vertical here
	if ( 1 + checkVector(coords.x, coords.y, 0, -1) + checkVector(coords.x, coords.y, 0, 1) == rowSize)
	{
		alert("Vertical Win!");
	}
}

function checkVector(xCoord, yCoord, xDelta, yDelta)
{
	var nextCellId = 'cell:'+(xCoord+xDelta)+','+(yCoord+yDelta);
	//If the next element exists and it is checked, we need to check the one after that
	if( document.getElementById(nextCellId) && document.getElementById(nextCellId).style.backgroundColor == CHECKED_COLOR)
	{
		return 1 + checkVector(xCoord+xDelta, yCoord+yDelta);
	}
	else
	{
		return 0;
	}
	
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