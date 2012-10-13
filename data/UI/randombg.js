function randomBg()
{
var hex1=new Array("db7491", "db9d74", "9174db", "74acdb", "74dbba", "74c6db", "db7474", "dbc474")
var bg="#"+hex1[Math.floor(Math.random()*hex1.length)]
return bg
}

function getInt(num){
	var integerNumber = parseInt(num);
	return  integerNumber
}
