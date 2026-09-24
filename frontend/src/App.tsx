import { Route, Routes } from "react-router-dom";
import Layout from "./components/Layout";
import Home from "./pages/Home";
import Search from "./pages/Search";
import Explore, { CaseMap, Comparator, CountryPage, RegionPage, CityPage, ContinentPage } from "./pages/Explore";
import Podcasts, { EpisodePage } from "./pages/Podcasts";
import Library from "./pages/Library";
import Memory from "./pages/Memory";
import CasePage, {
  DossierPage,
  VictimsPage,
  TimelinePage,
  InvestigationPage,
  EvidencePage,
  PsychologyPage,
  VictimologyPage,
  CaseMapPage,
  CourtPage,
  SourcesPage,
  MemorialPage,
  ExpertsPage,
  LessonsPage,
  WhatIfCasePage,
} from "./pages/Case";
import Psychology from "./pages/Psychology";
import Investigations from "./pages/Investigations";
import ColdCases from "./pages/ColdCases";
import Archives from "./pages/Archives";
import Training, { GlossaryPage, GlossaryEntryPage, CoursePage } from "./pages/Training";
import WhatIf, { WhatIfDetail } from "./pages/WhatIf";
import Ethics from "./pages/Ethics";
import Account from "./pages/Account";
import NotFound from "./pages/NotFound";

export default function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/rechercher" element={<Search />} />

        <Route path="/explorer" element={<Explore />} />
        <Route path="/explorer/continent/:continent" element={<ContinentPage />} />
        <Route path="/explorer/pays/:code" element={<CountryPage />} />
        <Route path="/explorer/pays/:code/region/:region" element={<RegionPage />} />
        <Route path="/explorer/pays/:code/ville/:city" element={<CityPage />} />
        <Route path="/explorer/carte" element={<CaseMap />} />
        <Route path="/explorer/comparateur" element={<Comparator />} />

        <Route path="/podcasts" element={<Podcasts />} />
        <Route path="/podcasts/:id" element={<EpisodePage />} />

        <Route path="/bibliotheque" element={<Library />} />
        <Route path="/memoire" element={<Memory />} />

        <Route path="/dossiers/:slug" element={<CasePage />} />
        <Route path="/dossiers/:slug/dossier" element={<DossierPage />} />
        <Route path="/dossiers/:slug/victimes" element={<VictimsPage />} />
        <Route path="/dossiers/:slug/chronologie" element={<TimelinePage />} />
        <Route path="/dossiers/:slug/enquete" element={<InvestigationPage />} />
        <Route path="/dossiers/:slug/indices" element={<EvidencePage />} />
        <Route path="/dossiers/:slug/psychologie" element={<PsychologyPage />} />
        <Route path="/dossiers/:slug/victimologie" element={<VictimologyPage />} />
        <Route path="/dossiers/:slug/carte" element={<CaseMapPage />} />
        <Route path="/dossiers/:slug/justice" element={<CourtPage />} />
        <Route path="/dossiers/:slug/sources" element={<SourcesPage />} />
        <Route path="/dossiers/:slug/memoire" element={<MemorialPage />} />
        <Route path="/dossiers/:slug/experts" element={<ExpertsPage />} />
        <Route path="/dossiers/:slug/lecons" element={<LessonsPage />} />
        <Route path="/dossiers/:slug/et-si" element={<WhatIfCasePage />} />

        <Route path="/psychologie" element={<Psychology />} />
        <Route path="/enquetes" element={<Investigations />} />
        <Route path="/cold-cases" element={<ColdCases />} />
        <Route path="/archives" element={<Archives />} />

        <Route path="/formation" element={<Training />} />
        <Route path="/formation/glossaire" element={<GlossaryPage />} />
        <Route path="/formation/glossaire/:slug" element={<GlossaryEntryPage />} />
        <Route path="/formation/:slug" element={<CoursePage />} />

        <Route path="/et-si" element={<WhatIf />} />
        <Route path="/et-si/:id" element={<WhatIfDetail />} />

        <Route path="/ethique" element={<Ethics />} />
        <Route path="/compte" element={<Account />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Layout>
  );
}
