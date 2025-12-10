// Embla Carousel Integration

const initCarousel = () => {
    const createCarousel = (rootNodeId, options = {}, plugins = []) => {
        const rootNode = document.querySelector(rootNodeId);
        if (!rootNode) return;

        // Add Embla classes programmatically if not present, to match expected structure
        // Expects structure:
        // .embla (rootNode)
        //   .embla__container
        //     .embla__slide

        // However, we are modifying HTML directly in the plan.
        // So here we just initialize.

        const viewportNode = rootNode.querySelector('.embla__viewport');
        if (!viewportNode) {
            console.warn(`Embla Carousel: Viewport not found for ${rootNodeId}`);
            return;
        }

        // Check if EmblaCarousel is defined (loaded via CDN)
        if (typeof EmblaCarousel === 'undefined') {
            console.error('Embla Carousel library not loaded.');
            return;
        }

        const embla = EmblaCarousel(viewportNode, options, plugins);

        // Navigation buttons
        const prevBtn = rootNode.querySelector('.embla__prev');
        const nextBtn = rootNode.querySelector('.embla__next');

        if (prevBtn && nextBtn) {
            const scrollPrev = () => embla.scrollPrev();
            const scrollNext = () => embla.scrollNext();

            prevBtn.addEventListener('click', scrollPrev);
            nextBtn.addEventListener('click', scrollNext);

            const updateButtons = () => {
                if (options.loop) return; // If loop is true, always enabled

                if (embla.canScrollPrev()) prevBtn.removeAttribute('disabled');
                else prevBtn.setAttribute('disabled', 'disabled');

                if (embla.canScrollNext()) nextBtn.removeAttribute('disabled');
                else nextBtn.setAttribute('disabled', 'disabled');
            };

            embla.on('select', updateButtons);
            embla.on('init', updateButtons);
        }
    };

    // Featured Tours Carousel (Homepage)
    createCarousel('#featured-tours-carousel', {
        loop: true,
        align: 'start',
        slidesToScroll: 1,
        breakpoints: {
            '(min-width: 768px)': { slidesToScroll: 2 },
            '(min-width: 1024px)': { slidesToScroll: 1 } // Actually it's 4 columns, we scroll 1 by 1 or more?
        }
    });

    // Related Tours Carousel (Tour Details)
    createCarousel('#related-tours-carousel', {
        loop: true,
        align: 'start',
        slidesToScroll: 1
    });
};

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', initCarousel);
