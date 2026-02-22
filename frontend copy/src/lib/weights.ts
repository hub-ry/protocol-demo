import { base } from '$app/paths';

export type WeightEntry = { date: string; weight: number };

const API_BASE = (import.meta as any).env?.VITE_API_URL as string | undefined;

/** Load body weight: from API when VITE_API_URL is set, else from static weight.json (no Tailscale). */
export async function getWeights(): Promise<WeightEntry[]> {
	if (API_BASE) {
		try {
			const res = await fetch(`${API_BASE.replace(/\/$/, '')}/weights`);
			if (res.ok) return await res.json();
		} catch {}
	}
	try {
		const res = await fetch(`${base}/weight.json`);
		if (res.ok) return await res.json();
	} catch {}
	return [];
}
