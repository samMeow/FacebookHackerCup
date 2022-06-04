const fs = require('fs');
const readline = require('readline');
const _ = require('lodash');
const outfile = "zombine.txt";

const cold_grep_data = (base_vec, range, data) => {
	return {
		base_vec: base_vec,
		data: _.filter(data, (val) => {
			let [x, y] = val;

			if(base_vec[0] < 0 || base_vec[1] < 0)
				return false;

			if( x >= base_vec[0] && x <= base_vec[0] + range && y >= base_vec[1]  && y<= base_vec[1] + range)
				return true;
			else 
				return false;
		}) 
	}
}

const cluster_data = (data, range) => {
	var tmp = [];
	_.each(data, (val)=>{
		let [x, y] = val;

		let progress = [
			cold_grep_data([x - range, y - range], range, data),
			cold_grep_data([x - range, y], range, data),
			cold_grep_data([x - range, y - range], range, data),
			cold_grep_data([x , y], range, data)
		];

		progress = _.filter(progress, (val)=> val.data.length >0 );

		tmp = _.unionWith(tmp, progress, (a,b)=> _.isEqual(a.base_vec, b.base_vec));
	});
	return tmp;
}

const combination = (clustered, clustered_max) => {
	var tmp = [];
	_.each(clustered, (a)=>{
		_.each(clustered, (b)=>{
			var com = {
				a_base_vec: a.base_vec,
				b_base_vec: b.base_vec,
				data_len: _.unionWith(a.data, b.data, _.isEqual).length,
				a_data: a.data,
				b_data: b.data
			}
			// if(com.data_len > clustered_max)
			tmp.push(com);
		})
	});
	return tmp;
}


const merge_square = (a, b, range) => {
	const b_min_x = _.reduce(b, (memo,val)=> Math.min(memo, val[0]), Infinity);
	const b_min_y = _.reduce(b, (memo,val)=> Math.min(memo, val[1]), Infinity);
	const b_max_x = _.reduce(b, (memo,val)=> Math.max(memo, val[0]), -1);
	const b_max_y = _.reduce(b, (memo,val)=> Math.max(memo, val[1]), -1);

	var min = 0;

	for(var i = b_max_x - range; i <= b_min_x; i++ ){
		for(var j = b_max_y - range; i <= b_min_y; j++){
			var tmp_data = _.map(b, (val) => [val[0] - i, val[j] - j]);
			var inter = _.intersectionWith(a, tmp_data, _.isEqual);
			if(inter.length == 0){
				min = 0;
				return min;
			}else{
				min = Math.min(min, inter.length);
			}
		}

	}
	return min;
}

const process_com = (com, range) => {
	var max = 0;
	for(var i = 0; i < com.length; i ++){
		let { a_data: a,
			b_data: b,
			a_base_vec: a_base,
			b_base_vec: b_base,
			data_len: len } = com[i];

		if(len <= max)
			break;

		var tmp_a = _.map(a, (val) => [val[0] - a_base[0], val[1] - a_base[1]]);
		var tmp_b = _.map(b, (val) => [val[0] - b_base[0], val[1] - b_base[1]]);
		max = Math.max(max, len - merge_square(tmp_a, tmp_b, range));
	}
	return max;
}

const process_data = (case_num, entry) => {
	let {r : range, data} = entry;

	var clustered = cluster_data(data, range);

	clustered = clustered.sort((a,b)=>{
		return b.data.length - a.data.length;
	});
	// console.log(clustered);
	clustered_max = clustered[0].data.length || 0;
	console.log(clustered.length);

	var com = combination(clustered, clustered_max);
	com.sort((a,b)=>{
		return b.data_len - a.data_len;
	});
	console.log(com.length);


	var max = process_com(com, range);
	fs.appendFileSync(outfile, output(case_num, max), 'utf8');
}

const output = (case_num, num) => {
	return "Case #" + case_num + ": " + num+'\n';
};


var readfile = (input_file) => {
	var case_num = 1,line_cnt = 0, how_many_line = 0;
	var buffer = {r:0, data:[]};
	const inputStream = readline.createInterface({
		input: fs.createReadStream(input_file)
	});

	inputStream.on('line',(line)=>{
		if(line_cnt > 0){
			var args = line.split(' ');
			if(how_many_line == 0 ){
				how_many_line = parseInt(args[0]);
				buffer.r = parseInt(args[1]);
			}else{
				var ints = _.map(args, (x) => parseInt(x))
				buffer.data.push(ints);
				how_many_line --;
				if(how_many_line == 0){
					process_data(case_num, buffer);
					case_num ++;
					buffer = {r:0, data:[]};
				}
			}
		}
		line_cnt ++;
	})
}

readfile(process.argv[2]);