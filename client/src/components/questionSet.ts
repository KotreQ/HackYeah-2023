export const questions = [
    {
        id: 0,
        title: 'Do jakiej szkoły średniej chcesz uczęszczać?',
        typeOfQuestion: 'single',
        answers: [
            ['Liceum', 5],
            ['Technikum', 5],
            ['Szkoła branżowa zawodowa', 5],
            ['Studia', 1],
        ],
    },
    {
        id: 1,
        title: 'Którego stopnia studia cię interesują?',
        typeOfQuestion: 'single',
        answers: [
            ['I stopnia', 2],
            ['II stopnia', 2],
            ['III stopnia', 2],
        ],
    },
    {
        id: 2,
        title: 'Którym rodzajem studiów jesteś zainteresowany?',
        typeOfQuestion: 'single',
        answers: [
            ['Studia stacjonarne', 3],
            ['Studia niestacjonarne', 4],
        ],
    },
    {
        id: 3,
        title: 'Czy potrzebujesz wynajęcia pokoju w akademiku?',
        typeOfQuestion: 'single',
        answers: [
            ['Tak', 4],
            ['Nie', 4],
        ],
    },
    {
        id: 4,
        title: 'Preferujesz studia płatne czy bezpłatne?',
        typeOfQuestion: 'single',
        answers: [
            ['Studia bezpłatne', 5],
            ['Studia płatne', 5],
        ],
    },
    {
        id: 5,
        title: 'Jakiej pomocy potrzebujesz?',
        typeOfQuestion: 'single',
        answers: [
            ['Pomoc z wybraniem kierunku', 6],
            ['Pomoc z wybraniem szkoły o wybranym kierunku', 7],
        ],
    },
    {
        id: 6,
        title: 'Wpisz interesujący cię kierunek',
        typeOfQuestion: 'text',
        answers: [['', 7]],
    },
    {
        id: 7,
        title: 'Czym się interesujesz?',
        typeOfQuestion: 'text',
        answers: [['']], // empty to detect end of quiz
    },
];
