const fs = require('fs');
const readline = require('readline')
const outfile = "tmp.txt";

var inCircle = (x, y, r) => {
	return ((x * x) + (y * y))  <= (r * r) ;
}

var point_to_radin = (x, y) => {
	var inPI;
	if(y >= 0){
		inPI= Math.atan2(y, x);
	}else{
		inPI= Math.atan2(y, x) + 2 * Math.PI;
	}
	return inPI / (2*Math.PI);
}


var radin_to_percentage = (radin) => {
	if(radin >= 0.25){
		return (1 - (radin - 0.25)) *100;
	}else{
		return (0.25 - radin) *100;
	}
}

var inSement = (percentage, x, y) => {
	// console.log(percentage, point_to_radin(x, y), radin_to_percentage(point_to_radin(x, y)));
	return (percentage >= radin_to_percentage(point_to_radin(x, y)));
}

var output = (num, inArea) => {
	var color = inArea ? 'black' : 'white';
	return "Case #" + num + ": " + color+'\n';
}

var main = (input_file) => {
	var i = 0;
	const inputStream = readline.createInterface({
		input: fs.createReadStream(input_file)
	});

	inputStream.on('line',(line)=>{
		var args = line.split(' ');
		if(args.length < 3)
			return;

		i++;
		var percentage = args[0];
		var x = args[1]-50;
		var y = args[2]-50;

		fs.appendFileSync(outfile, output(i, inCircle(x, y, 50) && inSement(percentage, x, y)), 'utf8')

	})
}

main(process.argv[2]);