import { ref } from "vue";

export class Query {

	data: any = [];
	current_question_id = ref(0);

	constructor() {
	}

	addData(data: any): any {
		this.data.push(data);
		console.log(this.data);
	}

	getData(): any {
		return this.data;
	}

	setData(data: any) {
		this.data = data;
	}
}
