<script setup lang="ts">
import { questions } from '@/components/questionSet.ts';
import SingleMultipleChoiceButton from '@/components/questions/SingleMultipleChoiceButton.vue';
import SubmitButton from '@/components/questions/SubmitButton.vue';
import TextEntry from '@/components/questions/TextEntry.vue';
import { Query } from '../query';

let query = new Query();
</script>

<style lang="scss">
@import '../../styles/index.scss';
</style>

<template>
    <div class="container">
        <div
            v-for="question in questions.slice(
                query.current_question_id.value,
                query.current_question_id.value + 1
            )"
        >
            <h2>
                {{ question.title }}
            </h2>

            <div class="question__answer-container">
                <div
                    class="question__answer"
                    v-for="(answer, index) in question.answers"
                    :key="index"
                >
                    <SingleMultipleChoiceButton
                        v-if="
                            question.typeOfQuestion == 'single' ||
                            question.typeOfQuestion == 'multiple'
                        "
                        :question_id="question.id"
                        :label="answer[0]"
                        :question_type="question.typeOfQuestion"
                        :next_question_id="answer[1]"
                        :query="query"
                    >
                    </SingleMultipleChoiceButton>
                </div>
                <TextEntry
                    v-if="question.typeOfQuestion == 'text'"
                    :question_id="question.id"
                    :next_question_id="answer[1]"
                    :query="query"
                >
                </TextEntry>

                <SubmitButton
                    v-if="
                        question.typeOfQuestion == 'multiple' ||
                        question.typeOfQuestion == 'text'
                    "
                    :question_id="question.id"
                    :question_type="question.typeOfQuestion"
                    :next_question_id="answer[1]"
                    :query="query"
                >
                </SubmitButton>
            </div>
        </div>
    </div>
</template>
