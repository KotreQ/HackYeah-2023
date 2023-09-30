<script lang="ts">

import {ref} from "vue";

const schoolGrade = ref('');

export default {
	props: ['query'],
	emits: ['on-submit'],
	methods: {
		submit() {
			this.query.addData({
				type: schoolGrade.value
			});

			this.$emit('on-submit');
		}
	},
	data() {
		return {schoolGrade};
	}
}

</script>

<template>
	<p>Jaki poziom szkoly?</p>

	<div class="flex flex-wrap gap-3">
		<div class="flex align-items-center">
			<RadioButton v-model="schoolGrade" inputId="schoolGradeMiddle" name="grade" value="middle"/>
			<label for="schoolGradeMiddle" class="ml-2">Szkoła średnia</label>
		</div>
		<div class="flex align-items-center">
			<RadioButton v-model="schoolGrade" inputId="schoolGradeStudies" name="grade" value="studies"/>
			<label for="schoolGradeStudies" class="ml-2">Studia</label>
		</div>
	</div>

	<Button icon="pi pi-check" aria-label="Submit" @click="submit()"/>
</template>

<style scoped>

</style>