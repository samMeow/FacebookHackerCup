const fs = require('fs');
const readline = require('readline');
const _ = require('lodash');
const outfile = "tmp.txt";


const output = (case_num, num) => {
	return "Case #" + case_num + ": " + num+'\n';
};


const cost = (num, idx) => {
	return num + (idx+1) * (idx+1) - (idx * idx);
}


const next_pick = (current_idx)  => {
	var tmp = [];
	var residue = 1;
	for (var i = 0; i < current_idx.length && residue > 0; i++, residue --){
		residue += current_idx[i] + 1;
		tmp.push([i, current_idx[i] + 1]);
	}
	return tmp;
}

const pick_min = (data, next_ava) => {
	var memo = [Infinity,[0,0]];

	_.each(next_ava, (val, idx)=>{
		let [i,j] = val;
		if(i > data.length -1)
			return;
		if(j > data.length -1)
			return;

		if(cost(data[i][j],j) < memo[0])
			memo = [ cost(data[i][j],j), val ]; 
	});

	return memo;
}

const pick_with_data = (data) => {
	const pick = (need, current_idx) => {

		var idx = current_idx.slice();
		var next_ava = next_pick(current_idx);

		var [min_data, [i,j]] = pick_min(data, next_ava);
		idx[i]++;

		if (need == 0){
			// console.log(x,y,cost(data[x][y], y))
			return min_data;
		}

		return min_data + pick(need -1, idx);
	}
	return pick;
}


const process_data = (case_num, data) => {
	data = _.map(data, (val, idx)=> val.sort((a,b)=> a - b));

	let need = data.length;
	// let current_min = _.reduce(data, (memo, val) => memo + val[0], 0);
	let current_idx_ar = _.fill(new Array(need), -1);
	var result = pick_with_data(data)(need-1, current_idx_ar);

	fs.appendFileSync(outfile, output(case_num, result), 'utf8');
}


var readfile = (input_file) => {
	var case_num = 1,line_cnt = 0, how_many_line = 0;
	var buffer = [];
	const inputStream = readline.createInterface({
		input: fs.createReadStream(input_file)
	});

	inputStream.on('line',(line)=>{
		if(line_cnt > 0){
			var args = line.split(' ');
			if(how_many_line == 0 ){
				
				how_many_line = parseInt(args[0]);
			}else{
				var ints = _.map(args, (x) => parseInt(x))
				buffer.push(ints);
				how_many_line --;
				if(how_many_line == 0){
					if(buffer.length > 0) {
						process_data(case_num, buffer);
						case_num ++;
						buffer = [];
					}
				}
			}
		}
		line_cnt ++;
	})
}

readfile(process.argv[2]);