import { describe, expect, it } from "vitest";
import { pick, tr } from "./i18n";

describe("YANIS//X bilingual content", () => {
  it("selects the requested language without inventing a value", () => {
    const value = { fr: "Fait", en: "Fact" };
    expect(pick(value, "fr")).toBe("Fait");
    expect(pick(value, "en")).toBe("Fact");
    expect(pick({ fr: "Seulement français" }, "en")).toBe("Seulement français");
  });

  it("keeps UI translations explicit", () => {
    expect(tr("fr", "nav.memory")).toBe("Mémoire");
    expect(tr("en", "nav.memory")).toBe("Memory");
    expect(tr("fr", "missing.key")).toBe("missing.key");
  });
});
