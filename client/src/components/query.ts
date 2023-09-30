export class Query {

	data: any = [];

	constructor() {
	}

	addData(data: any): any {
		this.data.push(data);
	}

	getData(): any {
		return this.data;
	}

	setData(data: any) {
		this.data = data;
	}
}
