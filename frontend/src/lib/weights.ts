import { demoWeights } from './demoWeights.js';

const API_BASE = typeof import.meta !== 'undefined' && (import.meta as any).env?.VITE_API_URL as string | undefined;

export type WeightEntry = { date: string; weight: number };

/**
 * Load weights: from API when VITE_API_URL is set and reachable, otherwise use demo data.
 * Use demo data for static deployment (e.g. GitHub Pages).
 */
export async function getWeights(): Promise<WeightEntry[]> {
	if (API_BASE) {
		try {
			const res = await fetch(`${API_BASE.replace(/\/$/, '')}/weights`);
			if (res.ok) return await res.json();
		} catch {
			// fall through to demo data
		}
	}
	return demoWeights;
}
