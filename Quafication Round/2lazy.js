const fs = require('fs');
const readline = require('readline');
const util = require('util');
const outfile = "lazy.txt";


var needed_load = (max, need = 50) => {
	return Math.ceil(need / max);
}

var find_possible = (ar)=>{
	var sort_ar = ar.sort((a,b)=> b - a);
	var head = 0, tail = sort_ar.length - 1;

	var possible = 0;
	for(;head < tail; head++){
		var need = needed_load(sort_ar[head]) - 1;
		if( head <= tail - need){
			possible++;
			tail -= need;
		}
	}
	return possible;
}

var output_format = (case_no, num) =>{
	return util.format('Case #%s: %s\n', case_no, num);
}

var main = (input_file) => {
	var i = 0, readline_cnt = 0, buffer = [];
	const inputStream = readline.createInterface({
		input: fs.createReadStream(input_file)
	});

	inputStream.on('line',(line)=>{
		if(readline_cnt == 0){
			i++;
			readline_cnt = parseInt(line);
			buffer = [];
		}else{
			readline_cnt--;
			buffer.push(parseInt(line));
			if(readline_cnt == 0){
				fs.appendFileSync(outfile, output_format(i, find_possible(buffer)), 'utf8');
			}
		}
	})
}

main(process.argv[2]);