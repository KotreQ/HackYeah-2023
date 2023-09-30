<template>
    <p>{{ props.label }}</p>
    <input type="radio" name="asdasdasdasd" value="{{ props.label }}" @click="click" />
</template>

<script setup lang="ts">
import { Query } from '../query';

const props = defineProps({
    question_id: Number,
    label: String,
    question_type: String,
    query: Query
});

function click() {
    if (props.question_type == "single") {
        // Send immediately to server
    }
    else if (props.question_type == "multiple") {
        // Store button data for later send
        props.query.addData([
            props.question_id,
            props.label
        ]);
    }
}
</script>

<style scoped>

</style>