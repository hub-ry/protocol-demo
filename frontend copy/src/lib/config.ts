import { base } from '$app/paths';

export type AppConfig = { userName: string; goalWeight: number };

const defaults: AppConfig = { userName: 'demo-user', goalWeight: 150 };

/** Load config from static config.json so updates deploy with the site. */
export async function getConfig(): Promise<AppConfig> {
	try {
		const res = await fetch(`${base}/config.json`);
		if (res.ok) {
			const data = await res.json();
			return {
				userName: data.userName ?? defaults.userName,
				goalWeight: Number(data.goalWeight) || defaults.goalWeight
			};
		}
	} catch {}
	return defaults;
}
