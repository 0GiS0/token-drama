export interface RankingEntry {
  position: number;
  emoji: string;
  label: string;
  badge: string;
  tokens: number;
}

export interface DailyCase {
  title: string;
  description: string;
  emoji: string;
}

export interface Streak {
  title: string;
  description: string;
  emoji: string;
}

export const rankings: RankingEntry[] = [
  { position: 1, emoji: "🎨", label: 'El que pide cambios de estilo 14 veces', badge: "🔥", tokens: 3200 },
  { position: 2, emoji: "✏️", label: 'El que reescribe el prompt 9 veces', badge: "🌧️", tokens: 2800 },
  { position: 3, emoji: "♾️", label: 'El que hace preguntas eternas', badge: "🌀", tokens: 2100 },
  { position: 4, emoji: "🤖", label: 'La IA que responde con un párrafo para decir sí', badge: "💬", tokens: 1200 },
  { position: 5, emoji: "🪄", label: 'El que añade "solo una cosita más" 12 veces', badge: "⭐", tokens: 542 },
];

export const dailyCase: DailyCase = {
  title: "Caso del día",
  description: "Prompt de 3 líneas convertido en saga de 27 mensajes",
  emoji: "📋",
};

export const streak: Streak = {
  title: "Racha más absurda",
  description: "6 respuestas seguidas para decidir un color de botón",
  emoji: "💬",
};

export const totalTokens = 9842;
export const chaosLevel = "Caos controlado";
