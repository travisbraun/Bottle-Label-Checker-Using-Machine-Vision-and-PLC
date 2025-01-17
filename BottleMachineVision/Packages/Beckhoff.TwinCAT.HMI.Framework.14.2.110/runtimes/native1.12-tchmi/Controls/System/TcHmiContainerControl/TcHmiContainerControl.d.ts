declare namespace TcHmi.Controls.System {
    class TcHmiContainerControl extends TcHmi.Controls.System.TcHmiControl {
        #private;
        /** Constructor */
        constructor(element: JQuery, pcElement: JQuery, attrs: TcHmi.Controls.ControlAttributeList);
        protected __widthMode: SizeModeWithContent | undefined;
        protected __heightMode: SizeModeWithContent | undefined;
        /**
         * If raised, the control object exists in control cache and constructor of each inheritation level was called.
         * This function is only to be used by the System. Other function calls are not intended.
         */
        __previnit(): void;
        /**
         * If raised, all attributes have been set to it's default or dom values.
         * This function is only to be used by the System. Other function calls are not intended.
         */
        __init(): void;
        /**
         * Is called by the system after the control instance gets part of the current DOM.
         * This function is only to be used by the System. Other function calls are not intended.
         */
        __attach(): void;
        /**
         * Is called by the system after the control instance is no longer part of the current DOM.
         * This function is only to be used by the System. Other function calls are not intended.
         */
        __detach(): void;
        /**
         * Destroy the current control instance.
         * Will be called automatically if system destroys control!
         */
        destroy(): void;
        /**
         * Sets __keepAlive
         * @param value
         */
        __setKeepAlive(value: boolean): void;
        /**
         * Adds a child to this control and handles the hierarchical management layer.
         * This base class does not append child's DOM element to the container DOM!
         * @param control Class instance of the child.
         * @param pos Optional index of the position for the new child.
         */
        addChild(control: TcHmi.Controls.System.baseTcHmiControl | undefined | null, pos?: number | null): void;
        /**
         * Adds a child to this control and handles the hierarchical management layer.
         * This base class does not append child's DOM element to the container DOM!
         * @param control Class instance of the child.
         * @param pos Optional index of the position for the new child.
         */
        __addChild(control: TcHmi.Controls.System.baseTcHmiControl, pos?: number | null): void;
        /**
         * Remove a child control.
         */
        removeChild(control: TcHmi.Controls.System.baseTcHmiControl | undefined | null): void;
        __removeChild(control: TcHmi.Controls.System.baseTcHmiControl): void;
        /**
         * Processes the current height and height unit.
         */
        __processHeight(callerControl?: TcHmiControl): void;
        /**
         * Processes the current width and width unit.
         */
        __processWidth(callerControl?: TcHmiControl): void;
        /**
         * Sets the value of the width mode attribute.
         * @param valueNew The new width mode value..
         */
        setWidthMode(valueNew: SizeModeWithContent | null): void;
        /**
         * Sets the value of the height mode attribute.
         * @param valueNew The new height mode value..
         */
        setHeightMode(valueNew: SizeModeWithContent | null): void;
        __getContentWidth(): number | null;
        __getContentHeight(): number | null;
    }
}
//# sourceMappingURL=TcHmiContainerControl.d.ts.map