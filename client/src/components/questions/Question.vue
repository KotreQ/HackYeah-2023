<script setup lang="ts">
import { questions } from "@/components/questionSet.ts";
import SingleMultipleChoiceButton from "@/components/questions/SingleMultipleChoiceButton.vue";
import { Query } from "../query";

let currentQuestionId = 2;

let query = new Query();
</script>

<template>
    <div class="container">
        <div v-for="question in questions" :key="question.id">
            <h2 v-if="question.id === currentQuestionId">
				{{ question.id }}
                {{ question.title }}
            </h2>

            <div
                class="answer"
                v-for="(answer, index) in question.answers"
                :key="index">

                <SingleMultipleChoiceButton
                    :question_id="question.id"
                    :label="answer"
                    :type="question.typeOfQuestion"
                    :query="query"
                ></SingleMultipleChoiceButton>
            </div>
        </div>
    </div>
</template>
