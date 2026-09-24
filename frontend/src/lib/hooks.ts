import { useCallback, useEffect, useRef, useState } from "react";
import { api, ApiError } from "./api";

/** Chargement de données avec états réels : loading / error / retry. */
export function useApi<T = any>(path: string | null, deps: any[] = []) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(Boolean(path));
  const [error, setError] = useState<string | null>(null);
  const [status, setStatus] = useState<number | null>(null);
  const seq = useRef(0);

  const load = useCallback(async () => {
    if (!path) {
      setLoading(false);
      return;
    }
    const id = ++seq.current;
    setLoading(true);
    setError(null);
    try {
      const r = await api.get<T>(path);
      if (id !== seq.current) return;
      setData(r);
      setStatus(200);
    } catch (e) {
      if (id !== seq.current) return;
      const err = e as ApiError;
      setError(err.message);
      setStatus(err.status);
      setData(null);
    } finally {
      if (id === seq.current) setLoading(false);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [path, ...deps]);

  useEffect(() => {
    load();
  }, [load]);

  return { data, loading, error, status, reload: load, setData };
}

/** Valeur mémorisée localement (préférences, filtres, avertissements). */
export function useLocal<T>(key: string, initial: T) {
  const [value, setValue] = useState<T>(() => {
    try {
      const raw = localStorage.getItem(key);
      return raw ? (JSON.parse(raw) as T) : initial;
    } catch {
      return initial;
    }
  });
  const set = useCallback(
    (v: T) => {
      setValue(v);
      try {
        localStorage.setItem(key, JSON.stringify(v));
      } catch {
        /* quota : la valeur reste en mémoire */
      }
    },
    [key],
  );
  return [value, set] as const;
}

export const fmtDate = (value: string, lang: string) => {
  if (!value) return "";
  const iso = /^\d{4}-\d{2}-\d{2}$/.test(value) ? value : null;
  if (iso) {
    try {
      return new Date(iso).toLocaleDateString(lang === "fr" ? "fr-FR" : "en-GB", {
        day: "2-digit",
        month: "long",
        year: "numeric",
      });
    } catch {
      return value;
    }
  }
  return value;
};
