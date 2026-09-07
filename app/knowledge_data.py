# knowledge_data.py
# -------------------------------------------------------
# All the upcycling knowledge that gets loaded into pgvector.
# I organized this as a list of dicts — each one is a "document"
# that gets embedded and stored for RAG retrieval.
# -------------------------------------------------------

UPCYCLING_KNOWLEDGE = [

    # ====== FABRIC TYPES ======
    {
        "category": "fabric",
        "title": "Cotton Fabric Properties",
        "content": (
            "Cotton is one of the best fabrics for upcycling projects. It's easy to cut, "
            "sew, and dye. Cotton holds dye well which makes it great for tie-dye and "
            "fabric painting projects. It frays moderately so you should use a zigzag stitch "
            "or pinking shears on raw edges. Cotton can be washed at high temperatures which "
            "helps when pre-treating old garments. Common cotton garments include t-shirts, "
            "jeans (cotton twill), button-down shirts, and bed sheets. Cotton blends with "
            "polyester are also common but won't absorb dye as well."
        ),
    },
    {
        "category": "fabric",
        "title": "Denim Fabric Properties",
        "content": (
            "Denim is a sturdy cotton twill fabric that's perfect for heavy-duty upcycling "
            "projects. It's thick and durable which makes it ideal for bags, pouches, and "
            "accessories that need structure. Denim comes in different weights — lightweight "
            "(4-8 oz) is easier to sew but heavyweight (12-16 oz) is more durable. You'll "
            "need a heavy-duty needle (size 16 or 18) and strong thread when sewing denim. "
            "Old jeans are the most common source. Denim can be distressed by sanding, "
            "bleaching, or cutting. The indigo dye in denim fades naturally which gives "
            "upcycled pieces a unique vintage look."
        ),
    },
    {
        "category": "fabric",
        "title": "Polyester and Synthetic Fabrics",
        "content": (
            "Polyester and other synthetic fabrics like nylon and acrylic have different "
            "properties than natural fibers. They don't absorb dye well (you need special "
            "disperse dyes for polyester). They melt when heated with an iron so always use "
            "low heat. Polyester doesn't fray as much as cotton which can be an advantage. "
            "Synthetic fabrics are more wrinkle-resistant and hold their shape well. They "
            "work well for accessories like bags and phone cases where durability matters. "
            "When cutting, use sharp scissors because dull ones will snag the fabric."
        ),
    },
    {
        "category": "fabric",
        "title": "Wool and Knit Fabrics",
        "content": (
            "Wool and knit fabrics need special handling during upcycling. Knits stretch "
            "which means you should use a ballpoint needle and stretch stitch on your sewing "
            "machine. Wool can be felted by washing in hot water and drying on high heat — "
            "this creates a thick, non-fraying material that's excellent for cutting into "
            "shapes without hemming. Old wool sweaters are commonly felted and then cut into "
            "mittens, hats, or ornaments. When working with knits, use fabric clips instead "
            "of pins to avoid creating holes. Always pre-wash knit garments before upcycling "
            "to account for shrinkage."
        ),
    },
    {
        "category": "fabric",
        "title": "Silk and Delicate Fabrics",
        "content": (
            "Silk and other delicate fabrics like chiffon and organza require careful handling. "
            "Use fine needles (size 9 or 11) and lightweight thread. These fabrics fray easily "
            "so French seams or serged edges are recommended. Silk can be painted with special "
            "silk dyes for beautiful artistic effects. Old silk scarves and blouses are great "
            "for making accessories like hair ties, pocket squares, or decorative patches. "
            "When cutting silk, place tissue paper underneath to prevent slipping. Iron on "
            "low heat with a pressing cloth."
        ),
    },

    # ====== TECHNIQUES ======
    {
        "category": "technique",
        "title": "Patchwork and Quilting Basics",
        "content": (
            "Patchwork is one of the easiest upcycling techniques — you combine pieces of "
            "different fabrics to create a new design. Start by cutting fabric into uniform "
            "shapes (squares, triangles, or hexagons). Use a 1/4 inch seam allowance. Press "
            "seams to one side, not open, for stronger joints. Quilting involves sandwiching "
            "batting between a patchwork top and a backing fabric. Chain piecing (sewing pieces "
            "one after another without cutting thread) speeds up the process. Patchwork is "
            "great for making blankets, pillow covers, bags, and wall hangings from old clothes."
        ),
    },
    {
        "category": "technique",
        "title": "T-Shirt Transformation Techniques",
        "content": (
            "T-shirts are the most commonly upcycled garment. Common transformations include: "
            "1) Crop top — mark a line where you want to crop, add 1 inch for hemming, cut "
            "straight across. 2) Tank top — cut off sleeves along the seam, optionally cut "
            "the neckline into a scoop or V-neck. 3) Tote bag — cut off sleeves, cut wider "
            "neckline for handle openings, sew bottom shut (turn inside out first). No-sew "
            "version: cut fringe along the bottom and tie knots. 4) Braided t-shirt — cut "
            "horizontal strips leaving one side intact, then stretch and braid. 5) Off-shoulder "
            "top — carefully cut the neckband and stretch it out."
        ),
    },
    {
        "category": "technique",
        "title": "Dyeing and Color Techniques",
        "content": (
            "Dyeing is one of the most effective ways to refresh old garments. Tie-dye works "
            "best on 100% cotton — use rubber bands to create patterns, apply fiber-reactive "
            "dyes, and let sit for 6-24 hours. Dip-dye creates an ombre effect by gradually "
            "dipping the garment into dye. Bleach techniques (reverse dye) work well on dark "
            "denim and cotton — use a spray bottle for splatter effects or stencils for designs. "
            "Natural dyes from avocado pits (pink), turmeric (yellow), or red cabbage (blue/purple) "
            "are eco-friendly but less colorfast. Always pre-wash garments, use hot water for "
            "better dye absorption, and rinse in cold water to set the color."
        ),
    },
    {
        "category": "technique",
        "title": "Embroidery and Surface Decoration",
        "content": (
            "Hand embroidery can transform a plain garment into something unique. Basic stitches "
            "to learn: backstitch (for outlines), satin stitch (for filling areas), French knot "
            "(for dots and texture), and chain stitch (for lines and borders). Use an embroidery "
            "hoop to keep fabric taut. Transfer designs using water-soluble stabilizer or by "
            "tracing with a disappearing ink pen. Embroidery works best on woven fabrics (not "
            "stretchy knits). Common projects: embroider florals on denim jackets, add monograms "
            "to shirt pockets, or cover stains and holes with decorative stitching. Use 2-3 "
            "strands of embroidery floss for most projects."
        ),
    },
    {
        "category": "technique",
        "title": "Deconstruction and Reconstruction",
        "content": (
            "Deconstruction means carefully taking apart a garment at its seams to get flat "
            "fabric pieces. Use a seam ripper to open seams without damaging the fabric. "
            "Remove collars, cuffs, pockets, and buttons — these are all reusable components. "
            "Once deconstructed, press all pieces flat and you have raw material for new projects. "
            "Reconstruction is about combining deconstructed pieces into new garments. For example, "
            "two old shirts can become one new shirt with contrasting panels. The key is to "
            "match fabric weights — don't combine heavy denim with lightweight cotton in a "
            "structural garment. Always interface lightweight fabrics when combining with heavier ones."
        ),
    },
    {
        "category": "technique",
        "title": "No-Sew Upcycling Methods",
        "content": (
            "Not everyone has a sewing machine, and that's fine. No-sew techniques include: "
            "1) Fabric glue — use for hems, patches, and attaching embellishments. Let dry 24 hours. "
            "2) Iron-on fusible webbing — great for appliques and hems. 3) Knotting and braiding — "
            "cut t-shirt material into strips and braid into bracelets, rugs, or bag handles. "
            "4) Safety pins — use as functional fasteners or decorative elements (punk style). "
            "5) Fabric tape — iron-on hemming tape for quick alterations. "
            "6) Fringing — cut parallel slits for a fringed edge on t-shirts, scarves, or bags. "
            "T-shirt yarn (cutting t-shirts into continuous strips) is great for crocheting without sewing."
        ),
    },

    # ====== PROJECT IDEAS ======
    {
        "category": "project",
        "title": "Bags and Totes from Old Clothes",
        "content": (
            "Bags are one of the most popular upcycling projects because they're practical and "
            "don't require exact sizing. Tote bag from t-shirt: turn inside out, sew bottom, "
            "cut handles from neckline and sleeves. Messenger bag from cargo pants: use the leg "
            "sections as the body, pockets become functional pockets on the bag, belt loops "
            "can hold a shoulder strap. Drawstring bag from any fabric: cut two rectangles, "
            "sew three sides, create a channel at the top for a drawstring cord. Laptop sleeve "
            "from an old sweater: use the body of a felted wool sweater, add padding, sew "
            "shut on three sides. Clutch from jeans: use the back pocket area, add a zipper."
        ),
    },
    {
        "category": "project",
        "title": "Home Decor from Upcycled Clothing",
        "content": (
            "Old clothes can become beautiful home decor. Throw pillow covers from button-down "
            "shirts — the button placket becomes the closure. T-shirt quilt — cut squares from "
            "favorite old tees and join them into a memory quilt. Fabric coasters — layer "
            "fabric scraps, quilt together, cut into circles or squares. Rag rug — cut old "
            "clothes into strips and braid into a circular or oval rug. Wall art — stretch "
            "interesting fabric (vintage tee graphics, patterned shirts) over canvas frames. "
            "Curtain tie-backs from neckties. Plant pot covers from sweater sleeves."
        ),
    },
    {
        "category": "project",
        "title": "Accessories from Old Garments",
        "content": (
            "Small accessories are perfect beginner upcycling projects. Scrunchies from fabric "
            "scraps — cut a rectangle, fold and sew into a tube, insert elastic, close the gap. "
            "Headbands from t-shirts — cut a strip, stretch it (t-shirt material curls into a "
            "cord). Fabric jewelry — braid strips into bracelets, wrap around bangles. Wallet "
            "from a shirt cuff — the button closure becomes the wallet closure. Phone case from "
            "jeans back pocket — add padding and a flap closure. Keychains from leather scraps. "
            "Belt from multiple neckties braided together. Bow tie from fabric scraps — cut two "
            "rectangles, one large for the bow and one small for the center wrap."
        ),
    },
    {
        "category": "project",
        "title": "Kids Clothing from Adult Garments",
        "content": (
            "Adult garments have enough fabric to make multiple kids' clothing items. A men's "
            "dress shirt can become a toddler dress — the shirt front with buttons becomes "
            "the dress front, sleeves become puff sleeves. A women's maxi skirt can be "
            "refashioned into a child's sundress. Jeans can become kids' shorts or skirts. "
            "T-shirt onesies — trace around an existing onesie on an old tee, cut and sew. "
            "The key is to use the existing hems and seams where possible to reduce finishing "
            "work. Always pre-wash adult garments before cutting to avoid shrinkage issues "
            "after the kids' garment is complete."
        ),
    },

    # ====== TOOLS ======
    {
        "category": "tools",
        "title": "Essential Sewing Tools for Upcycling",
        "content": (
            "The basic toolkit for upcycling includes: 1) Fabric scissors — sharp, dedicated "
            "to fabric only (never use on paper). 2) Seam ripper — essential for taking apart "
            "garments at the seams. 3) Measuring tape — flexible, at least 60 inches. "
            "4) Pins and pin cushion — or fabric clips for knits and delicates. 5) Hand sewing "
            "needles — assorted sizes for different fabrics. 6) Thread — polyester all-purpose "
            "thread works for most projects. 7) Chalk or disappearing ink marker — for marking "
            "cut lines. 8) Iron and ironing board — pressing seams makes a huge difference in "
            "the final look. 9) Ruler or quilting square — for straight lines and right angles. "
            "Nice to have: rotary cutter and cutting mat, pinking shears, and a basic sewing machine."
        ),
    },
    {
        "category": "tools",
        "title": "Sewing Machine Tips for Beginners",
        "content": (
            "If you have a sewing machine, even a basic one, it will speed up your upcycling "
            "projects a lot. Important settings: use a straight stitch (length 2.5mm) for most "
            "woven fabrics, a zigzag stitch for stretch fabrics and preventing fraying, and a "
            "basting stitch (length 4-5mm) for temporary seams. Always backstitch at the start "
            "and end of a seam to lock the stitches. Change your needle based on fabric type — "
            "universal for woven, ballpoint for knits, denim needle for heavy fabrics. Tension "
            "should usually stay on the default (4-5) unless you see loops on the bottom. "
            "Clean the bobbin area regularly, especially after sewing denim which produces lint. "
            "Practice on scrap fabric before sewing your actual project."
        ),
    },

    # ====== SUSTAINABILITY ======
    {
        "category": "sustainability",
        "title": "Textile Waste and Environmental Impact",
        "content": (
            "The fashion industry is one of the largest polluters globally. About 92 million "
            "tonnes of textile waste is generated each year worldwide. In India alone, roughly "
            "8 million tonnes of textile waste is generated annually. The average garment is "
            "worn only 7-10 times before being discarded. Fast fashion has accelerated this — "
            "fashion brands now produce nearly twice the amount of clothing compared to 20 years "
            "ago. Synthetic fabrics like polyester can take up to 200 years to decompose in "
            "landfills. Textile dyeing is the second largest polluter of water globally. By "
            "upcycling clothes instead of discarding them, we reduce landfill waste, save the "
            "water and energy needed to produce new garments, and reduce carbon emissions."
        ),
    },
    {
        "category": "sustainability",
        "title": "Circular Fashion Principles",
        "content": (
            "Circular fashion is about keeping clothes in use as long as possible. The hierarchy "
            "is: 1) Reduce — buy fewer, better quality items. 2) Reuse — wear clothes longer, "
            "swap with friends, buy secondhand. 3) Repair — fix buttons, patch holes, mend seams. "
            "4) Upcycle — transform old garments into new items with added value. 5) Recycle — "
            "as a last resort, send textile fibers for industrial recycling. Upcycling sits high "
            "in this hierarchy because it adds creative value and extends garment life without "
            "industrial processing. Each upcycled garment represents saved water (2,700 liters "
            "to make one cotton t-shirt), saved energy, and prevented emissions."
        ),
    },

    # ====== DIFFICULTY GUIDELINES ======
    {
        "category": "difficulty",
        "title": "Easy Upcycling Projects (Beginner Level)",
        "content": (
            "Easy projects require minimal tools and skills. They usually involve simple cuts "
            "and no or very basic sewing. Examples: t-shirt tote bag (no-sew knotted version), "
            "t-shirt crop top (just cutting), fabric scrunchies, braided t-shirt headbands, "
            "denim coasters (cut circles from jeans, stack and edge), tie-dye projects, "
            "simple patches and appliques with iron-on adhesive. Time estimate: 15-45 minutes. "
            "Good for people who have never sewn before. These projects typically use t-shirts "
            "and simple cotton garments which are the easiest materials to work with."
        ),
    },
    {
        "category": "difficulty",
        "title": "Medium Difficulty Upcycling Projects",
        "content": (
            "Medium projects require some sewing skills (straight seams, basic machine use) "
            "and more planning. Examples: lined tote bag with pockets, throw pillow covers from "
            "shirts, simple skirt from a t-shirt, drawstring bags, laptop sleeves, patchwork "
            "table runners, basic embroidery on denim jackets. Time estimate: 1-3 hours. "
            "You should be comfortable with a sewing machine or be able to do neat hand stitches. "
            "These projects often involve combining multiple garments or adding elements like "
            "zippers, buttons, or linings."
        ),
    },
    {
        "category": "difficulty",
        "title": "Hard Upcycling Projects (Advanced Level)",
        "content": (
            "Hard projects require pattern-making skills, advanced sewing techniques, and often "
            "multiple sessions to complete. Examples: restructured jackets or coats, tailored "
            "garments from deconstructed pieces, quilts from many fabric pieces, structured bags "
            "with multiple compartments, corset-style tops from shirts, patchwork denim jacket "
            "from multiple jeans. Time estimate: 4-20+ hours. These projects often involve "
            "fitting, darts, set-in sleeves, interfacing, and precise measurements. Knowledge "
            "of garment construction is essential. The results are impressive and can look "
            "professional when done well."
        ),
    },

    # ====== GARMENT SPECIFIC TIPS ======
    {
        "category": "garment_tips",
        "title": "Upcycling Jeans and Denim",
        "content": (
            "Jeans are upcycling gold — they're durable and versatile. Top projects from old "
            "jeans: 1) Cut-off shorts — mark the length, add 1 inch, cut, fray edges by washing. "
            "2) Denim skirt — open the inner leg seam, overlap front and back, sew flat. "
            "3) Apron — use the top half (waistband becomes the apron ties). 4) Pencil case — "
            "use a leg section with a zipper added at the top. 5) Denim quilt — cut squares "
            "from multiple jeans in different washes. The waistband, belt loops, and pockets "
            "are all reusable elements. Denim's weight makes it self-supporting for bags and "
            "accessories. Use heavy-duty thread (upholstery thread works great) for denim projects."
        ),
    },
    {
        "category": "garment_tips",
        "title": "Upcycling Dress Shirts and Button-Downs",
        "content": (
            "Dress shirts have great tailored pieces that can be reused. The collar can be "
            "removed and worn as a Peter Pan collar accessory. The cuffs make excellent small "
            "pouches or bracelets. The button placket can be reused as a closure for bags or "
            "pillow covers. Full shirt transformations: halter top (remove sleeves and back, "
            "tie at neck), off-shoulder blouse (remove collar, widen neckline), apron "
            "(use the front panel with buttons as the apron front). The back yoke area is "
            "usually the largest unblemished fabric piece, perfect for cutting into other patterns."
        ),
    },
    {
        "category": "garment_tips",
        "title": "Upcycling Sweaters and Knitwear",
        "content": (
            "Sweaters are excellent for cozy upcycling projects. Felting wool sweaters (wash "
            "on hot, dry on hot) creates a dense, non-fraying material that cuts like fabric. "
            "Projects from felted sweaters: mittens (trace your hand shape), hat (use the bottom "
            "ribbing as the hat brim), Christmas stockings, coasters, phone cases, and stuffed "
            "animals. Non-felted sweater projects: sweater pillow (stuff and sew opening shut), "
            "leg warmers (cut off sleeves), pet sweater (adapt the body). When cutting knit "
            "sweaters that aren't felted, sew a line of stitching first to prevent unraveling, "
            "then cut outside the stitching line."
        ),
    },
    {
        "category": "garment_tips",
        "title": "Upcycling Leather and Faux Leather",
        "content": (
            "Leather and faux leather can't be sewn with regular techniques — pin holes are "
            "permanent in real leather. Use leather needles, binder clips instead of pins, and "
            "a Teflon or roller presser foot on your sewing machine. Old leather jackets are "
            "valuable for upcycling — the leather panels can become wallets, journal covers, "
            "coasters, earrings, or bag panels. Faux leather is easier to work with but can "
            "crack or peel over time. For hand stitching leather, pre-punch holes with an awl "
            "and use waxed thread. Leather edges can be finished with edge paint or burnishing. "
            "Clean old leather with leather conditioner before cutting to restore flexibility."
        ),
    },

    # ====== CARE & PREP ======
    {
        "category": "preparation",
        "title": "Preparing Garments for Upcycling",
        "content": (
            "Proper preparation makes a big difference in the final product. Steps: "
            "1) Inspect the garment — check for stains, holes, thin spots, and pilling. "
            "2) Wash thoroughly — use hot water (if fabric allows) to pre-shrink and clean. "
            "3) Remove unwanted elements — cut off tags, remove shoulder pads, take off buttons "
            "you want to reuse. 4) Iron the garment flat — this makes measuring and cutting "
            "much more accurate. 5) Identify the usable areas — mark around stains or damage "
            "that you'll need to avoid. 6) Consider the grain — fabric has a lengthwise grain "
            "(parallel to selvage) that affects how it drapes and stretches. Cut with the grain "
            "for stability or on the bias (45 degrees) for stretch and drape."
        ),
    },
    {
        "category": "preparation",
        "title": "Dealing with Stains and Damage",
        "content": (
            "Don't discard garments just because of stains or minor damage — these can be "
            "worked around or incorporated into the design. Strategies: 1) Cut around the damage — "
            "plan your pattern pieces to avoid stained areas. 2) Cover it up — use embroidery, "
            "patches, or appliques over stains and small holes. Japanese boro stitching and "
            "sashiko embroidery are beautiful techniques specifically designed for visible mending. "
            "3) Bleach it out — for light-colored cotton, try targeted bleach application. "
            "4) Dye over it — a darker dye can hide many stains. 5) Embrace it — some damage "
            "adds character, especially in denim where distressing is fashionable. Remember: "
            "the goal of upcycling is not perfection, it's creativity and sustainability."
        ),
    },
]
