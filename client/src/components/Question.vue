<script setup lang="ts">
import {ref, shallowRef} from "vue";
import StudyLevel from "@/components/questions/SchoolGradeQuestion.vue";
import {Query} from "@/components/query";

const questionComponent = shallowRef(StudyLevel);

let query = new Query();

function questionSubmitted() {
	console.log(JSON.stringify(query.getData()));
}

</script>

<template>
	<component :is="questionComponent" @on-submit="questionSubmitted" :query="query"></component>
</template>

<style scoped>

</style>