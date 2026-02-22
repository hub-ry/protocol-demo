import { base } from '$app/paths';

export type UpperEntry = { date: string; value: number };

const API_BASE = (import.meta as any).env?.VITE_API_URL as string | undefined;

/** Load upper (bench press) data: from API when set, else from static upper.json. */
export async function getUpper(): Promise<UpperEntry[]> {
	if (API_BASE) {
		try {
			const res = await fetch(`${API_BASE.replace(/\/$/, '')}/upper`);
			if (res.ok) return await res.json();
		} catch {}
	}
	try {
		const res = await fetch(`${base}/upper.json`);
		if (res.ok) return await res.json();
	} catch {}
	return [];
}
