import Link from 'next/link';
import { Brain } from 'lucide-react';

export default function Navbar() {
    return (
        <nav className="bg-white border-b border-gray-200 sticky top-0 z-50">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex justify-between h-16">
                    <div className="flex">
                        <Link href="/" className="flex-shrink-0 flex items-center gap-2">
                            <Brain className="h-8 w-8 text-indigo-600" />
                            <span className="font-bold text-xl tracking-tight text-gray-900">Mental Models</span>
                        </Link>
                    </div>
                    <div className="flex items-center">
                        <Link href="/" className="text-gray-500 hover:text-gray-900 px-3 py-2 rounded-md text-sm font-medium">
                            Catalog
                        </Link>
                        <Link href="/about" className="text-gray-500 hover:text-gray-900 px-3 py-2 rounded-md text-sm font-medium">
                            About
                        </Link>
                    </div>
                </div>
            </div>
        </nav>
    );
}
