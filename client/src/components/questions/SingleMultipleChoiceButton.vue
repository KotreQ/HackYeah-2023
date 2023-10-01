<template>
    <Button
        @click="click"
    >{{ props.label }}</Button>
</template>

<style>
.p-button {
    padding: 5px 10px;
}
</style>

<script setup lang="ts">
import { Query } from '../query';

const props = defineProps({
    question_id: Number,
    label: String,
    question_type: String,
    next_question_id: Number,
    query: Query,
});

function click() {
    props.query.addData([props.question_id, props.label]);
    props.query.current_question_id.value = props.next_question_id;
    console.log(props.query.current_question_id.value);
}
</script>
