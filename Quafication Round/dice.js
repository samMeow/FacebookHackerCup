const fs = require('fs');
const readline = require('readline')
const _ = require('underscore');
const outfile = "zobine.txt";


var factorial = _.memoize((n) => {
	if(n <= 1)
		return 1;
	return n * factorial(n-1);
})

var nCr = (n, r) => {
	var ran = _.range(n -r + 1, n+1);

	var factor = _.reduce(ran, (memo, k)=>{
		return memo * k;
	},1);

	// console.log(factor);
	return factor / factorial(r);
	// return factorial(n) / (factorial(r) * factorial(n-r));
}



var pob = (p, size, num) => {
	var max = Math.floor( (p - num) / size) + 1;

	if(max < 0)
		return 0;

	var base = Math.pow(size, num);

	var range = _.range(max);

	var factor = _.reduce(range, (memo, k)=>{
		var ne = k % 2 == 0 ? 1 : -1;
		return memo + ne * nCr(num, k) * nCr(p - size * k -1, num -1);
	}, 0);

	return factor / base;

}

var lower_pob = (p, size, num) => {
	if(p <  num)
		return 0;
	if(p > size * num)
		return 1;
	var range = _.range(num, p);
	return _.reduce(range, (memo, k) => {
		// console.log(k, pob(k, size, num));
		return memo + pob(k, size, num);
	},0)
}

var readInput = (min, x, y, z) => {
	// console.log(arguments);
	var local_min = min- z;
	return lower_pob(local_min, y, x)
}

var string_to_args = (str)=>{
	var [x, rest] = str.split('d');

	if(rest.indexOf('+') > -1){
		var [y, z] = rest.split("+");
		var ar = [x, y, z];
	}else if(rest.indexOf('-') > -1){
		var [y, z] = rest.split("-");
		var ar = [x, y, -z];
	}else{
		var ar = [x, rest, 0];
	}
	return _.map(ar, (v,idx) => parseInt(v));
}


var round6 = (num) => {
	return Math.round(num * 1000000) / 1000000;
}

var extend6 = (num) =>{
	return num.toFixed(6)
}

var output = (num, p) => {
	return "Case #" + num + ": " + extend6(round6(p))+'\n';
}

var main = (input_file) => {
	var i = 0;
	var cnt = 0;
	const inputStream = readline.createInterface({
		input: fs.createReadStream(input_file)
	});

	var min;
	inputStream.on('line',(line)=>{
		if(cnt > 0){
			var args = line.split(' ');
			if(cnt % 2 == 1){
				i++;
				min = args[0];
			}else{
				var final = _.reduce(args, (memo, str)=>{
					var small_args = [min].concat(string_to_args(str));
					return Math.max(memo, 1 - readInput.apply(null, small_args));
				},0);
				fs.appendFileSync(outfile, output(i, final), 'utf8')
			}
		}
		cnt ++;
	});	
}

main(process.argv[2]);





