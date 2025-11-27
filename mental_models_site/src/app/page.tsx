import Link from 'next/link';
import { getSortedModelsData } from '@/lib/api';
import Navbar from '@/components/Navbar';

export default function Home() {
    const allModels = getSortedModelsData();

    // Group models by first letter
    const groupedModels: { [key: string]: typeof allModels } = {};
    allModels.forEach(model => {
        const firstLetter = model.title.charAt(0).toUpperCase();
        // Handle numbers or other chars
        const key = /^[A-Z]/.test(firstLetter) ? firstLetter : '#';
        if (!groupedModels[key]) {
            groupedModels[key] = [];
        }
        groupedModels[key].push(model);
    });

    const sortedKeys = Object.keys(groupedModels).sort((a, b) => {
        if (a === '#') return 1;
        if (b === '#') return -1;
        return a.localeCompare(b);
    });

    return (
        <div className="min-h-screen bg-gray-50">
            <Navbar />
            <main className="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
                <div className="text-center mb-12">
                    <h1 className="text-4xl font-extrabold text-gray-900 sm:text-5xl sm:tracking-tight lg:text-6xl">
                        Master Your Thinking
                    </h1>
                    <p className="mt-5 max-w-xl mx-auto text-xl text-gray-500">
                        A curated collection of mental models to help you make better decisions, solve problems, and understand the world.
                    </p>
                </div>

                {/* A-Z Index */}
                <div className="flex flex-wrap justify-center gap-2 mb-12 sticky top-20 z-40 bg-gray-50 py-4">
                    {sortedKeys.map(letter => (
                        <a key={letter} href={`#${letter} `} className="px-3 py-1 text-sm font-medium text-indigo-600 bg-white rounded-md shadow-sm hover:bg-indigo-50 border border-gray-200">
                            {letter}
                        </a>
                    ))}
                </div>

                <div className="space-y-16">
                    {sortedKeys.map(letter => (
                        <div key={letter} id={letter} className="scroll-mt-24">
                            <h2 className="text-2xl font-bold text-gray-900 mb-6 border-b border-gray-200 pb-2">{letter}</h2>
                            <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
                                {groupedModels[letter].map((model) => (
                                    <Link key={model.slug} href={`/models/${model.slug}`} className="group block h-full">
                                        <div className="bg-white overflow-hidden shadow rounded-lg hover:shadow-md transition-shadow duration-300 h-full flex flex-col border border-gray-100">
                                            <div className="px-4 py-5 sm:p-6 flex-grow">
                                                <h3 className="text-lg leading-6 font-bold text-gray-900 group-hover:text-indigo-600 transition-colors">
                                                    {model.title}
                                                </h3>
                                                <p className="mt-2 text-sm text-gray-500 line-clamp-3">
                                                    Explore the concept of {model.title} and how it applies to your life.
                                                </p>
                                            </div>
                                            <div className="bg-gray-50 px-4 py-4 sm:px-6">
                                                <span className="text-xs font-medium text-indigo-600 uppercase tracking-wider">
                                                    Read Summary &rarr;
                                                </span>
                                            </div>
                                        </div>
                                    </Link>
                                ))}
                            </div>
                        </div>
                    ))}
                </div>
            </main>
        </div>
    );
}
