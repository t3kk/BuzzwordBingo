/*Functions for the bingo game*/

function bingoCellClicked(clickedId)
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
