export const questions = [
    {
        id: 0,
        title: 'Do jakiej szkoły średniej chcesz uczęszczać?',
        typeOfQuestion: 'multiple',
        answers: [
            ['Liceum', 6],
            ['Technikum', 6],
            ['Szkoła branżowa zawodowa', 6],
            ['Studia', 2],
        ],
    },
    {
        id: 2,
        title: 'Którego stopnia studia cię interesują?',
        typeOfQuestion: 'single',
        answers: [
            ['I stopnia', 3],
            ['II stopnia', 3],
            ['III stopnia', 3],
        ],
    },
    {
        id: 3,
        title: 'Którym rodzajem studiów jesteś zainteresowany?',
        typeOfQuestion: 'single',
        answers: [
            ['Studia stacjonarne', 4],
            ['Studia niestacjonarne', 5],
        ],
    },
    {
        id: 4,
        title: 'Czy potrzebujesz wynajęcia pokoju w akademiku?',
        typeOfQuestion: 'single',
        answers: [
            ['Tak', 5],
            ['Nie', 5],
        ],
    },
    {
        id: 5,
        title: 'Preferujesz studia płatne czy bezpłatne?',
        typeOfQuestion: 'single',
        answers: [
            ['Studia bezpłatne', 6],
            ['Studia płatne', 6],
        ],
    },
    {
        id: 6,
        title: 'Jakiej pomocy potrzebujesz?',
        typeOfQuestion: 'single',
        answers: [
            ['Pomoc z wybraniem kierunku', 7],
            ['Pomoc z wybraniem szkoły o wybranym kierunku', 8],
        ],
    },
    {
        id: 7,
        title: 'Wpisz interesujący cię kierunek',
        typeOfQuestion: 'text',
        answers: [['', 8]],
    },
    {
        id: 8,
        title: 'Czym się interesujesz?',
        typeOfQuestion: 'text',
        answers: [['']], // empty to detect end of quiz
    },
];
