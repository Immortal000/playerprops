import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
	return {
		data: {
			title: 'Player Props',
			playerStats: {
				'2024-11-28': [],
				'2024-11-29': [
					{
						date: '11/29/2024',
						line: 21.5,
						name: 'LeBron James',
						last10: '60%',
						last5: '50%',
						lastheadtohead: '80%',
						position: 'under'
					},
					{
						date: '11/29/2024',
						line: 25.5,
						name: 'Stephen Curry',
						last10: '65%',
						last5: '70%',
						lastheadtohead: '55%',
						position: 'over'
					}
				],
				'2024-11-30': [
					{
						date: '11/30/2024',
						line: 18.5,
						name: 'Ja Morant',
						last10: '45%',
						last5: '40%',
						lastheadtohead: '65%',
						position: 'over'
					}
				]
			},
			timestamp: new Date().toISOString()
		}
	};
};
