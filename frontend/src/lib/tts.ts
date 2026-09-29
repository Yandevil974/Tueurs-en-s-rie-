/**
 * Moteur vocal de synthèse embarqué (Web Speech API).
 * 
 * Permet à l'application de lire à voix haute n'importe quel épisode,
 * qu'il dispose ou non d'un fichier audio préenregistré.
 * Fonctionne nativement sur Android (moteur Google TTS intégré au Z Fold 5).
 */

class TTSPlayer {
  private synth: SpeechSynthesis | null = null;
  private utterance: SpeechSynthesisUtterance | null = null;
  private isSpeaking = false;
  private currentVoice: SpeechSynthesisVoice | null = null;

  constructor() {
    if (typeof window !== "undefined" && "speechSynthesis" in window) {
      this.synth = window.speechSynthesis;
      this.initVoices();
    }
  }

  private initVoices() {
    if (!this.synth) return;
    const loadVoices = () => {
      const voices = this.synth?.getVoices() || [];
      // Chercher une voix française naturelle
      this.currentVoice =
        voices.find((v) => v.lang.startsWith("fr") && (v.name.includes("Google") || v.name.includes("Natural"))) ||
        voices.find((v) => v.lang.startsWith("fr")) ||
        null;
    };

    loadVoices();
    if (this.synth.onvoiceschanged !== undefined) {
      this.synth.onvoiceschanged = loadVoices;
    }
  }

  public speak(text: string, onEnd?: () => void) {
    if (!this.synth) return;
    this.stop();

    this.utterance = new SpeechSynthesisUtterance(text);
    this.utterance.lang = "fr-FR";
    this.utterance.rate = 1.0;
    this.utterance.pitch = 1.0;
    if (this.currentVoice) {
      this.utterance.voice = this.currentVoice;
    }

    this.utterance.onend = () => {
      this.isSpeaking = false;
      onEnd?.();
    };

    this.utterance.onerror = () => {
      this.isSpeaking = false;
    };

    this.isSpeaking = true;
    this.synth.speak(this.utterance);
  }

  public pause() {
    if (this.synth && this.isSpeaking) {
      this.synth.pause();
    }
  }

  public resume() {
    if (this.synth) {
      this.synth.resume();
    }
  }

  public stop() {
    if (this.synth) {
      this.synth.cancel();
      this.isSpeaking = false;
    }
  }

  public isAvailable(): boolean {
    return this.synth !== null;
  }
}

export const tts = new TTSPlayer();
