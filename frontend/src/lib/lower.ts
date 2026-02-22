import { base } from '$app/paths';

export type LowerEntry = { date: string; value: number };

const API_BASE = (import.meta as any).env?.VITE_API_URL as string | undefined;

/** Load lower (squat) data: from API when set, else from static lower.json. */
export async function getLower(): Promise<LowerEntry[]> {
	if (API_BASE) {
		try {
			const res = await fetch(`${API_BASE.replace(/\/$/, '')}/lower`);
			if (res.ok) return await res.json();
		} catch {}
	}
	try {
		const res = await fetch(`${base}/lower.json`);
		if (res.ok) return await res.json();
	} catch {}
	return [];
}
