/*Functions for the bingo game*/


var CHECKED_COLOR = 'rgb(100, 149, 237)';  /* Using rgb value for cornflowerblue to fix comparison.  Can we get the icon in cornflower blue https://www.youtube.com/watch?v=746j4dN1sQg */
var UNCHECKED_COLOR = 'white';
//TODO: set rowsize dynaically
var rowSize = 5;

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
	if(1 + checkVector(coords.x, coords.y, 0, 1) + checkVector(coords.x, coords.y, 0, -1)==rowSize)
	{
		alert("WIN! vert");
	}
	if(1 + checkVector(coords.x, coords.y, 1, 0) + checkVector(coords.x, coords.y, -1, 0)==rowSize)
	{
		alert("WIN! hor");
	}
	//This checks for a decending line in the table.  Coordinates x and y both increase though.
	//This is because the cell ids are assigned top to bottom.
	if(1 + checkVector(coords.x, coords.y, 1, 1) + checkVector(coords.x, coords.y, -1, -1)==rowSize)
	{
		alert("WIN! negSlope");
	}
	if(1 + checkVector(coords.x, coords.y, 1, -1) + checkVector(coords.x, coords.y, -1, 1)==rowSize)
	{
		alert("WIN! posSlope");
	}
}

function checkVector(xCoord, yCoord, xDelta, yDelta)
{
	var nextCellId = 'cell:'+(xCoord+xDelta)+','+(yCoord+yDelta);
	//If the next element exists and it is checked, we need to check the one after that
	if( document.getElementById(nextCellId) && document.getElementById(nextCellId).style.backgroundColor == CHECKED_COLOR)
	{
		return 1 + checkVector(xCoord+xDelta, yCoord+yDelta, xDelta, yDelta);

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
  return {x:parseInt(m[1]), y:parseInt(m[2])}
}
