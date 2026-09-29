import { describe, expect, it } from "vitest";
import { getEmbeddedPayload } from "./data";

describe("offline Android API bundle", () => {
  it("serves the updated catalogue and map without access-tier metadata", async () => {
    const cases = await getEmbeddedPayload("/cases");
    const world = await getEmbeddedPayload("/explore");
    const europe = await getEmbeddedPayload("/explore/continent/Europe");

    expect(cases?.count).toBe(8);
    expect(cases?.cases).toHaveLength(8);
    expect(JSON.stringify(cases)).not.toMatch(/\"(tier|premium|locked)\"/i);
    expect(world?.continents).toEqual(expect.arrayContaining([
      expect.objectContaining({ name: "Europe" }),
    ]));
    expect(europe?.level).toBe("continent");
    expect(europe?.countries.length).toBeGreaterThan(0);
  });

  it("supports filters and interactive answers offline", async () => {
    const usCases = await getEmbeddedPayload("/cases?country=US");
    const search = await getEmbeddedPayload("/search?q=Gr%C3%A9gory");
    const answer = await getEmbeddedPayload("/questions/1/answer", {
      method: "POST",
      body: JSON.stringify({ choice: "b" }),
    });

    expect(usCases?.cases.length).toBeGreaterThan(0);
    expect(usCases?.cases.every((item: any) => item.country === "US")).toBe(true);
    expect(search?.results.some((result: any) => result.type === "case")).toBe(true);
    expect(answer?.choice).toBe("b");
    expect(answer?.explanation).toBeTruthy();
  });
});
